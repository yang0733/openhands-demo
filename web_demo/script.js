document.addEventListener("DOMContentLoaded", () => {
    const dataContainer = document.getElementById("data-container");

    // Function to fetch a joke from an API
    async function fetchJoke() {
        try {
            dataContainer.innerHTML = "<p>Fetching a new joke...</p>";
            const response = await fetch("https://icanhazdadjoke.com/", {
                headers: {
                    "Accept": "application/json"
                }
            });
            const data = await response.json();
            dataContainer.innerHTML = `
                <p class="joke-text">${data.joke}</p>
                <p class="joke-id">Joke ID: ${data.id}</p>
            `;
        } catch (error) {
            dataContainer.innerHTML = `<p style="color: red;">Failed to fetch joke: ${error.message}</p>`;
            console.error("Error fetching joke:", error);
        }
    }

    fetchJoke();

    // Optionally, refresh the joke every few seconds
    // setInterval(fetchJoke, 10000);
});
