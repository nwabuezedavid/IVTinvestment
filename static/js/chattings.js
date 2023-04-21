const container = document.querySelector('.message-con')
const inputmessage = document.querySelector('.inputmessage')
const btnsub = document.querySelector('.btnsub')
const token = document.querySelector('.token')
const idUser = document.querySelector('.idUser').innerHTML
const isactives = document.querySelector('.isactive').innerHTML
console.log(idUser);
let innerh =""
const urls = 'http://127.0.0.1:8000/fetchclientmassage'
function mainchatbvox(chat) {
    let ins = []
    chat.forEach(e => {
        let check =  e.usersender == isactives
        if (idUser == e.roomid) {
            ins.push( e.message)
            
        innerh +=`
        <div class="user-sending sdddda">
        <p class="client" >${check ?   e.message:  ''}
            
            </p>
    </div>
    <div class="friend-sending  sdddda"  >
        <p >
        ${check ? ''  :  e.message}</p>
    </div>
    
        `
    }

    
});
container.innerHTML +=  innerh
let childd = document.querySelectorAll('.sdddda ')
let child = document.querySelectorAll('.sdddda p')
innerh =""

console.log(child, 'sldl');
    child.forEach((element,val) => {
        
        // console.log(String(elemesnt),ins);
        if (element.innerHTML.match(/[a-z]/  )|| element.innerHTML.match(/[A-Z]/  )  ) {
            // element.classList.remove('hiddend')
            element.style.display="flex"
            childd[val].style.margin= '0'

        }
        else if (Number(element.textContent.length) <1   ) {
            // element.classList.remove('hiddend')
            element.style.display="flex"
            childd[val].style.margin= '0'

            Number(element.textContent.length)
        }
        else{
            element.style.display="none"
            // element.classList.add('hiddend')

        }
    });
}
function ajaxdeposite() {
    
    fetch(urls +`/${idUser}/`)
    .then(res => res.json())
    .then(data  =>{
        
        
        console.log(data.data);
        mainchatbvox(data.data)
       
      
    })
    
    
    
}
ajaxdeposite()
btnsub.addEventListener('click',e =>{
    e.preventDefault()
    
    fetch(urls +`/${idUser}/`,{
        method:"POST",
        headers:{
            'Content-Type' :'application/json',
            'X-CSRFToken':token.value,
        },
        body: JSON.stringify({
            message: inputmessage.value,
            usersender: isactives,
            roomid: idUser,
         
    
        })
    })
    .then(resp => resp.json())
    .then(data => {
    postArr = []
    postArr.push(data)
    mainchatbvox(postArr)
    }
    
        )
        inputmessage.value = ''
    })