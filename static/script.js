document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    if(form){

        form.addEventListener("submit", () => {

            const button = document.querySelector("button");

            button.innerText = "Generating Itinerary...";

            button.disabled = true;

        });

    }

});