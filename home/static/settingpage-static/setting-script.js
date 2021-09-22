console.log("setting script");

const logoutbutton = document.getElementById("logoutUser");

logoutbutton.addEventListener('click',()=>{
   
    console.log("Logging out.... ");

    const data_send = { 
        logout:"True",
     };
    let url = '../api/logout/' 
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
      if(data_recieved[0].logout){
        //logout the user
        window.location.replace("../login");
        }else{
          alert("Problem Exist Check Console")
        }
    })
    .catch((error) => {
      console.error('Error:', error);
    });

});