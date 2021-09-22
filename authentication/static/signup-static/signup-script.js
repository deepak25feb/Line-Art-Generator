console.log("signup script");

const username = document.getElementById("username");
const emailid = document.getElementById("email");
const password = document.getElementById("password");
const submit = document.getElementById("submit");

submit.addEventListener("click", () => {
    const userData = username.value;
    const emailidData = emailid.value;
    const passwordData = password.value;
    // console.log(userData, emailidData, passwordData);

    const data_send = { 
         username:userData,
         password:passwordData,
         emailid:emailidData
     };
    //Request
    let url = '../api/signup/' ;
    fetch(url, {
      method: 'POST', // or 'PUT'
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data_send),
    })
    .then(response => response.json())
    .then(data_recieved => {
      console.log('RESPONSE :', data_recieved);
      const p = document.getElementById("errormessage");
      let responseObj = data_recieved[0]
      if(!responseObj.error){
        //User is Valid
        // Session Generated
        window.location.replace("../");  // Redirect
        p.innerHTML = "Correct";
      }else{
        //User is InValid
        if(responseObj.emailid_status == "valid"){
          if(responseObj.username_status == "invalid"){
          p.innerHTML = "Username should be Unique"
          }
        }else{
          p.innerHTML = "Email ID should be Unique"
        }
        
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });

});
