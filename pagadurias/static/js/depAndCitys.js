function populateDepartments(allData, currentObj) {

        let departamentos = [...new Set(allData.map(data => data.departamento))];

        currentObj.innerHTML = '<option value="">-- Seleccione un Departamento --</option>';

        departamentos.forEach(dep => {
            let option = document.createElement("option");
            option.value = dep;
            option.textContent = dep;
            currentObj.appendChild(option);
        });
    }

function populateCities(department, allData, citysObj) {
    let ciudades = allData
        .filter(data => data.departamento === department)
        .map(city => city.municipio);

    ciudades.forEach(city => {
        let option = document.createElement("option");
        option.value = city;
        option.textContent = city;
        citysObj.appendChild(option);
    });
}

async function fetchDepartmentsAndCities() {
    showLoadingOverlay();  // Muestra el loader

    const url = "https://www.datos.gov.co/resource/xdk5-pm3f.json";

    try {
        await new Promise(resolve => setTimeout(resolve, 300)); // simula demora

        const response = await fetch(url);
        if (!response.ok) {
            throw new Error("Error al obtener departamentos y ciudades");
        }

        return await response.json();
    } catch (error) {
        const loadingText = document.getElementById("loadingText");
        if (loadingText) loadingText.textContent = "❌ Error al cargar datos";
    } finally {
        hideLoadingOverlay(); // Oculta el loader
    }
}