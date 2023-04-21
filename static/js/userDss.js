const click__poc = document.querySelector(".toogle__fixed__top")
const click__con__pic = document.querySelector(".fixed")
const sec__1 = document.querySelector(".sec-1")
const sec__2 = document.querySelector(".sec-2")
const click__sec__1 = document.querySelector(".click__sec__1")
const click__sec__1__colse = document.querySelector(".cose")
sec__1.classList.add("sec__1___close") 
click__sec__1.addEventListener("click",()=>{
    sec__1.classList.toggle("sec__1___close")
    sec__2.style.width = '100vw'
})
click__sec__1__colse.addEventListener("click",()=>{
    sec__1.classList.add("sec__1___close")
    sec__2.style.width = '100vw'
    
})

click__poc.addEventListener("click",()=>{
    click__con__pic.classList.toggle("open__fixed")
})


const btcsele = document.querySelectorAll('.outMethioc')
const allaret = document.querySelector('.alart')
const dfd = document.querySelectorAll('.allCoinpayment')

const paymentconsec = document.querySelectorAll('.paymentconsec')
let isactive = 'true'
function alertmessage(e) {
  
    console.log(isactive);
    allaret.classList.add('alerhidden')
    allaret.innerHTML = e
}


console.log();

dfd.forEach((es,s) => {
btcsele.forEach((e, val) => {
    
    e.addEventListener('click',(es)=>{
           if (s == val) {
               console.log(dfd[val].value);
               paymentconsec[val].classList.toggle('agt')
                   es.target.classList.toggle('agt')
                    const agt = document.querySelectorAll('.agt')

                   agt.length
                   let textmessage = ''

                   if (agt.length > 2) {
                     textmessage = 'you can not select two payment gateway'
                     paymentconsec.forEach(element => {
                        element.classList.remove('agt')
                     });
                     dfd.forEach(element => {
                        element.value = ""
                     });
                     setTimeout(() => {
                        allaret.classList.remove('alerhidden')
                        allaret.style.color= 'red !important '
                        isactive = "true"
                        location.reload()
                    },6000);
                }else{
                   
                     textmessage = `You select  ${dfd[val].value} as your payment method `
                }
                
                alertmessage(textmessage)
          if (es.target.classList.contains("agt") ) {
              
              setTimeout(() => {
                  allaret.classList.remove('alerhidden')
                  isactive = "true"
              },6000);
            }
                   
                }  
                  
                        })
  }); 
});









console.log(location.pathname );
    const spansds = document.querySelectorAll(".spansd")
    spansds.forEach((e, vla)=>{
            e.classList.remove("spansdopen")
        
        e.addEventListener('click',(es)=>{
            es.preventDefault()
            e.classList.toggle("spansdopen") 
            const ds = document.querySelectorAll(".spansdopen")
console.log(ds.length);
            // e.classList.add("spansdopen")
            
            if ( e.previousElementSibling) {
                
                e.previousElementSibling.classList.remove('spansdopen')
            } 
   
            if( es.nextElementSibling){

                e.nextElementSibling.classList.remove('spansdopen') 
            } 
            
            if (Number(ds.length) > 1) {
                alert('You can select only one plan')
                e.classList.remove('spansdopen') 
                location.reload()
            }

        })
    })
  function domainfun () {
    
    const domain  =  location.hostname
    const domaincon = document.querySelector('.domain')
    let val = domaincon.value =  domain
    console.log(domaincon.value);
  }
  domainfun()