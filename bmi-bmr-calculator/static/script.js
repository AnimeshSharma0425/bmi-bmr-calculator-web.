const form = document.getElementById("calc-form");
const submitBtn = document.getElementById("submit-btn");
const errorBox = document.getElementById("error");
const resultBox = document.getElementById("result");

const bmiEl = document.getElementById("bmi");
const categoryEl = document.getElementById("category");
const bmrEl = document.getElementById("bmr");
const caloriesEl = document.getElementById("calories");

const BADGE_CLASS = {
  "Underweight": "underweight",
  "Normal weight": "normal",
  "Overweight": "overweight",
  "Obesity": "obesity",
};

function showError(text) {
  errorBox.textContent = text;
  resultBox.classList.add("hidden");
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorBox.textContent = "";

  const payload = {
    age: parseInt(document.getElementById("age").value, 10),
    gender: document.getElementById("gender").value,
    weight: parseFloat(document.getElementById("weight").value),
    height: parseFloat(document.getElementById("height").value),
    activity: parseInt(document.getElementById("activity").value, 10),
  };

  submitBtn.disabled = true;
  submitBtn.textContent = "Calculating...";

  try {
    const res = await fetch("/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json().catch(() => ({}));

    if (!res.ok) {
      // 400 gives a text message; 422 (validation) gives a list
      const msg = typeof data.detail === "string"
        ? data.detail
        : "Please check the values you entered.";
      showError(msg);
      return;
    }

    bmiEl.textContent = data.bmi;
    categoryEl.textContent = data.category;
    categoryEl.className = "badge " + (BADGE_CLASS[data.category] || "");
    bmrEl.textContent = data.bmr.toFixed(2);
    caloriesEl.textContent = data.daily_calories.toFixed(2);
    resultBox.classList.remove("hidden");
  } catch {
    showError("Could not reach the server. Please try again.");
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Calculate";
  }
});
