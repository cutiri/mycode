//const API_URL = "http://127.0.0.1:2224/api";
//const API_URL = "https://aux1-3cc49d54-2d5b-4ae0-bb2f-26a05a442f54.live.alta3.com/api"
const API_URL = "/api"
const sendBtn = document.getElementById("send_btn");
const mainInput = document.getElementById("command");
let inputText = "";
let inputValues = [];
let inputValuesCurrentAutocomplete = 0;


// sendBtn.addEventListener("click", () => {
//     alert("button pressed")
// });

mainInput.addEventListener("keydown", (e) => {
    if (e.key === 'Tab' && mainInput.value){
        e.preventDefault();
        fetch(`${API_URL}/autocomplete/${mainInput.value}`)
            .then((response) => response.json())
            .then((json) => {
                if (inputText != mainInput.value){
                    inputValues = Object.values(json)[0];
                    if(inputValues && inputValues.length > 0){
                        mainInput.value = inputValues[0];
                        console.log(inputValues)
                        console.log(inputValues[0])
                    }
                    inputText = mainInput.value;
                }
            })
            .catch((err) => {
                console.log(`Error fetching ${API_URL}/autocomplete/${mainInput.value}`)
            })
    }
})