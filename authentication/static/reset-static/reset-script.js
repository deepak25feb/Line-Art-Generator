console.log("reseting Password")

const emailid = document.getElementById("email");
const c_password_ele = document.getElementById("c_password");
const n_password_ele = document.getElementById("n_password");
const submit = document.getElementById("submit");



submit.addEventListener("click", () => {
    const emailidData = emailid.value;
    const c_passwordData = c_password_ele.value;
    const n_passwordData = n_password_ele.value;
    console.log("Client Entered Data : ",emailidData, c_passwordData,n_passwordData);

    const data_send = { 
        emailid:emailidData,
        c_password:c_passwordData,
        n_password:n_passwordData
    };
    //Request
    // let url = '../../api/'  ---> both absolute and relative works
    let url = '../api/resetGuestUser/' 
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
      if(!data_recieved[0].error){ //False --> If every thing is correct
        if(data_recieved[0].c_password_status){
            p.innerHTML = "Password Changed";
        }
      }else{
        p.innerHTML = "Email ID or Password is Incorrect"
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });

});