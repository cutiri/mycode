const API_URL = "http://localhost:2224/api";
const sendBtn = document.getElementById("send_btn");
const mainInput = document.getElementById("main_input");
let inputText = "";
let inputValues = [];
let inputValuesCurrentAutocomplete = 0;


sendBtn.addEventListener("click", () => {
    alert("button pressed")
});

mainInput.addEventListener("keydown", (e) => {
    if (e.key === 'Tab' && mainInput.value){
        e.preventDefault();
        fetch(`${API_URL}/autocomplete/${mainInput.value}`)
            .then((response) => response.json())
            .then((json) => {
                if (inputText != mainInput.value){
                    inputValues = Object.values(json);
                    inputText = mainInput.value;
                }
            })
            .catch((err) => {
                console.log(`Error fetching ${API_URL}/autocomplete/${mainInput.value}`)
            })
    }
})