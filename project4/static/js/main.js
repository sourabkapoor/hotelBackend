function loginUser(){
  formData = {
    email: "sourabkapoor@gmail.com",
    password: "zxcvbnm"
  }
  fetch("http://127.0.0.1:8000/login/", {
    method: "POST",
    headers: {'Content-Type': 'application/json'}, 
    body: JSON.stringify(formData)
    }
  )
  .then(res => res.json())
  .then(res => console.log("res is : ", res))
}