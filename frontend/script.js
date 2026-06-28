async function generateBranding() {

    const idea = document.getElementById("idea").value;

    const response = await fetch("http://127.0.0.1:8000/generate",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            description:idea
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
    <div class="card">
        <h2>${data.name}</h2>
        <h3>${data.tagline}</h3>

        <p><b>Idea:</b> ${data.description}</p>

        <p><b>Brand Colors:</b> ${data.colors}</p>

        <p><b>Logo Idea:</b> ${data.logo}</p>

        <p><b>Target Audience:</b> ${data.audience}</p>

        <p><b>Marketing Strategy:</b> ${data.marketing}</p>

    </div>
    `;
}