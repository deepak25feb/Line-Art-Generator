console.log("login script");

const emailid = document.getElementById("email");
const password = document.getElementById("password");
const submit = document.getElementById("submit");



submit.addEventListener("click", () => {
    const emailidData = emailid.value;
    const passwordData = password.value;
    console.log("Client Entered Data : ",emailidData, passwordData);

    const data_send = { 
        emailid:emailidData,
        password:passwordData
     };
    //Request
    // let url = '../../api/'  ---> both absolute and relative works
    let url = '../api/login/' 
    fetch(url, {
      method: 'POST', // or 'PUT'
      headers: {
        'Content-Type': 'application/json',
        //  'Referrer-Policy':'same-origin'
      },
      body: JSON.stringify(data_send),
    })
    .then(response => response.json())
    .then(data_recieved => {
      console.log('RESPONSE:', data_recieved);

      const p = document.getElementById("errormessage");
      if(data_recieved[0].userexist){
        if(!data_recieved[0].password){
          p.innerHTML = "UserName or Password Incorrect";
        }else{
          // Genrate Session
          // Redirect
          window.location.replace("../");  // If User is Genuine  it will redirect to home page i.e localhost:8000/home
          p.innerHTML = "Correct"; //Optional [testing purpose only]
          
        }

      }else{
        p.innerHTML = "User Doesn't Exist"
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });

});


