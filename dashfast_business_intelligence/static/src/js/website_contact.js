/** @odoo-module **/

console.log("DASHFAST JS CARGADO");

function mostrarMensajeExito(formulario) {
    formulario.innerHTML = `
        <div class="alert alert-success text-center p-5 rounded shadow-sm" role="alert">
            <h3 class="mb-3">Muchas gracias</h3>
            <p class="mb-0">
                Hemos recibido tu solicitud correctamente.
            </p>
            <p class="mb-0">
                La consulta SQL se ha generado y guardado correctamente.
            </p>
        </div>
    `;
}

async function enviarFormularioDashFast(formulario, event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
        event.stopImmediatePropagation();
    }

    console.log("Enviando formulario a Python...");

    const formData = new FormData(formulario);

    try {
        const response = await fetch("/dashfast/guardar_sql", {
            method: "POST",
            body: formData,
            credentials: "same-origin",
        });

        const text = await response.text();

        console.log(text);

        if (!response.ok) {
            alert("Error al ejecutar el script Python.");
            return;
        }

        mostrarMensajeExito(formulario);

    } catch (error) {
        console.error("Error enviando el formulario:", error);
        alert("Error al enviar el formulario.");
    }
}

function prepararFormularioDashFast() {
    const tablaSelect = document.getElementById("tabla");

    if (!tablaSelect) {
        return;
    }

    const formulario = tablaSelect.closest("form");

    if (!formulario) {
        console.log("No se encontró el formulario");
        return;
    }

    formulario.setAttribute("action", "/dashfast/guardar_sql");
    formulario.setAttribute("method", "post");

    formulario.removeAttribute("data-model_name");
    formulario.removeAttribute("data-success-mode");
    formulario.removeAttribute("data-success-page");

    formulario.classList.remove("s_website_form");
    formulario.classList.add("o_dashfast_sql_form");

    const modelInput = formulario.querySelector('input[name="model_name"]');
    if (modelInput) {
        modelInput.remove();
    }

    console.log("Formulario DashFast preparado");
}

document.addEventListener("DOMContentLoaded", prepararFormularioDashFast);
setTimeout(prepararFormularioDashFast, 500);
setTimeout(prepararFormularioDashFast, 1500);

document.addEventListener(
    "submit",
    function (event) {
        const formulario = event.target;

        if (!formulario || !formulario.querySelector("#tabla")) {
            return;
        }

        enviarFormularioDashFast(formulario, event);
    },
    true
);

document.addEventListener(
    "click",
    function (event) {
        const boton = event.target.closest(".o_dashfast_send");

        if (!boton) {
            return;
        }

        const formulario = boton.closest("form");

        if (!formulario || !formulario.querySelector("#tabla")) {
            return;
        }

        enviarFormularioDashFast(formulario, event);
    },
    true
);