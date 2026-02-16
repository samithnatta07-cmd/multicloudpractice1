const API_URL = "http://APP-ALB-DNS"; // backend ALB or proxy URL

function loadSkills() {
    fetch(`${API_URL}/skills`)
        .then(res => res.json())
        .then(data => {
            let html = "<ul>";
            data.forEach(skill => html += `<li>${skill}</li>`);
            html += "</ul>";
            document.getElementById("skills").innerHTML = html;
        });
}

function loadCerts() {
    fetch(`${API_URL}/certifications`)
        .then(res => res.json())
        .then(data => {
            let html = "<ul>";
            data.forEach(cert => html += `<li>${cert}</li>`);
            html += "</ul>";
            document.getElementById("certifications").innerHTML = html;
        });
}

function loadProjects() {
    window.open(`${API_URL}/projects`, "_blank");
}
