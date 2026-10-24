// ============================
// AI TRAITORS GAME JAVASCRIPT
// ============================

console.log("AI Traitors game.js loaded");


// ============================
// TIMER
// ============================

let time = 60;

const timer = document.getElementById("timer");

if (timer) {

    const interval = setInterval(() => {

        time--;

        timer.innerText = time;

        if (time <= 0) {

            clearInterval(interval);

            timer.innerText = "TIME UP";
        }

    }, 1000);
}


// ============================
// AI MESSAGE ANIMATION
// ============================

function showAIMessage(element) {

    if (!element) {
        return;
    }

    element.style.opacity = "0";

    element.style.transform = "translateY(10px)";

    setTimeout(() => {

        element.style.transition = "all 0.4s ease";

        element.style.opacity = "1";

        element.style.transform = "translateY(0)";

    }, 100);
}