document.getElementById("tripForm")
.addEventListener("submit", async function(event) {

    event.preventDefault();

    let destination =
        document.getElementById("destination").value;

    let budget =
        document.getElementById("budget").value;

    let days =
        document.getElementById("days").value;

    let interest =
        document.getElementById("interest").value;
        document.getElementById("result").innerHTML =
"<h2>Generating Trip...</h2>";

    let response = await fetch(
        "http://127.0.0.1:5000/plan-trip",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                destination,
                budget,
                days,
                interest
            })
        }
    );

    let data = await response.json();

    document.getElementById("result").innerHTML = `

        <h2>Your AI Trip Plan</h2>

        <pre>${data.trip}</pre>

    `;

});