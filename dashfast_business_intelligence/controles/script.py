from odoo import http
from odoo.http import request

from pathlib import Path
from datetime import datetime
import re
import unicodedata


class DashFastWebsiteController(http.Controller):

    @http.route('/dashfast/guardar_sql', type='http', auth='public', website=True, methods=['GET', 'POST'], csrf=True)
    def guardar_sql(self, **post):

        if request.httprequest.method == 'GET':
            return self._text_response("RUTA OK")

        email = (post.get('email_from') or '').strip()
        tabla = (post.get('tabla') or '').strip().lower()
        fecha_inicio = (post.get('fecha_inicio') or '').strip()
        fecha_fin = (post.get('fecha_fin') or '').strip()

        if not email:
            return self._text_response("Error: no se recibió el correo.")

        if tabla not in ('ventas', 'compras'):
            return self._text_response("Error: la tabla debe ser 'ventas' o 'compras'.")

        if not fecha_inicio or not fecha_fin:
            return self._text_response("Error: debes indicar fecha inicio y fecha fin.")

        if fecha_inicio > fecha_fin:
            return self._text_response("Error: la fecha inicio no puede ser mayor que la fecha fin.")

        cr = request.env.cr
        cr.execute(
            """
            SELECT id, name, email
            FROM res_partner
            WHERE LOWER(email) = LOWER(%s)
            ORDER BY id
            LIMIT 1
            """,
            (email,)
        )
        partner = cr.fetchone()

        if not partner:
            return self._text_response(
                f"No se encontró ninguna empresa/proveedor con el email: {email}"
            )

        partner_id = partner[0]
        partner_name = partner[1]

        if tabla == 'ventas':
            sql_generada = f"""
SELECT
    pt.name AS producto,
    sol.product_uom_qty AS cantidad,
    sol.price_unit AS precio_unitario,
    sol.price_subtotal AS total_venta,
    so.date_order AS fecha_venta
FROM sale_order_line sol
JOIN sale_order so
    ON so.id = sol.order_id
JOIN product_product pp
    ON pp.id = sol.product_id
JOIN product_template pt
    ON pt.id = pp.product_tmpl_id
JOIN product_supplierinfo psi
    ON psi.product_tmpl_id = pt.id
   AND (psi.product_id IS NULL OR psi.product_id = pp.id)
JOIN res_partner rp
    ON rp.id = psi.partner_id
WHERE rp.id = {partner_id}
  AND so.date_order::date >= {self._sql_quote(fecha_inicio)}
  AND so.date_order::date <= {self._sql_quote(fecha_fin)}
ORDER BY so.date_order DESC;
""".strip()

            tabla_nombre_archivo = "Ventas"

        else:
            sql_generada = f"""
SELECT
    pt.name AS producto,
    pol.product_qty AS cantidad,
    pol.price_unit AS precio_unitario,
    pol.price_subtotal AS total_compra,
    po.date_order AS fecha_compra
FROM purchase_order_line pol
JOIN purchase_order po
    ON po.id = pol.order_id
JOIN product_product pp
    ON pp.id = pol.product_id
JOIN product_template pt
    ON pt.id = pp.product_tmpl_id
WHERE po.partner_id = {partner_id}
  AND po.date_order::date >= {self._sql_quote(fecha_inicio)}
  AND po.date_order::date <= {self._sql_quote(fecha_fin)}
ORDER BY po.date_order DESC;
""".strip()

            tabla_nombre_archivo = "Compras"

        module_root = Path(__file__).resolve().parents[1]
        search_dir = module_root / "search"
        search_dir.mkdir(parents=True, exist_ok=True)

        empresa_limpia = self._sanitize_filename_part(partner_name)
        timestamp = datetime.now().strftime("%d%m%Y_%H_%M_%S")
        filename = f"{empresa_limpia}_{tabla_nombre_archivo}_{timestamp}.sql"
        file_path = search_dir / filename

        file_path.write_text(sql_generada, encoding="utf-8")

        respuesta = (
            "SQL generada correctamente\n\n"
            f"Empresa detectada: {partner_name}\n"
            f"Partner ID: {partner_id}\n"
            f"Tabla elegida: {tabla}\n"
            f"Fecha inicio: {fecha_inicio}\n"
            f"Fecha fin: {fecha_fin}\n"
            f"Archivo guardado: {filename}\n"
            f"Ruta: {file_path}\n\n"
            "Contenido del archivo:\n\n"
            f"{sql_generada}"
        )

        return self._text_response(respuesta)

    def _sanitize_filename_part(self, value):
        if not value:
            return "SinNombre"

        value = unicodedata.normalize("NFKD", value)
        value = "".join(char for char in value if not unicodedata.combining(char))
        value = value.replace(" ", "_")
        value = value.replace(".", "")
        value = re.sub(r"[^A-Za-z0-9_-]", "", value)
        value = re.sub(r"_+", "_", value).strip("_")

        return value or "SinNombre"

    def _sql_quote(self, value):
        if value is None:
            return "NULL"

        escaped = str(value).replace("'", "''")
        return f"'{escaped}'"

    def _text_response(self, text):
        return request.make_response(
            text,
            headers=[('Content-Type', 'text/plain; charset=utf-8')]
        )