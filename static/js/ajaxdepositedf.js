const  containerholder = document.querySelector('.dp-pending')
const  iduser = document.querySelector('.iddiplay').textContent
urls = 'http://127.0.0.1:8000/fetchdeposite'

const nex = document.querySelector('.nex')
console.log(urls  + '/iduser/');
let depositehtml  =''
console.log(9);
let start = 5
function deposite (allpend) {
    
    allpend.forEach((e,val) => {

        if (e.aproved ) {
            depositehtml += `<div class="dp-pending-con rd">
                            
            <big>${e.transittionuudi} </big>
            <big>USD  ${e.amount}.00 </big>
            <big>${e.dateDepsited}</big>
            <big>02 sep 2022 20:23</big>
            <big> approved maturity</big>
    
        </div>`
        } else {
            depositehtml += `<div class="dp-pending-con rd">
                            
            <big>${e.transittionuudi} </big>
            <big>USD  ${e.amount}.00 </big>
            <big>${e.dateDepsited}</big>
            <big>02 sep 2022 20:23</big>
            <big>pending approval</big>
        </div>`
        }
        
    });
    
    containerholder.innerHTML+=depositehtml
    let child = containerholder.querySelectorAll('.rd')
    function checttotel() {
        
        if ( start <= child.length  ) {
            nex.style.display="flex"
        }
        else{
            nex.style.display="none"
    
        }
        child.forEach((ea,valsa) => {
    
            ea.classList.display ="none"
    
        })
    }
    
    
    
    checttotel()
    
    function sjd() {
        child.forEach((ea,valsa) => {
            if (valsa <= start & start >= valsa ){
                ea.classList.remove('hiddens')
                
            } else if(valsa >= start - start){
                ea.classList.add('hiddens')

            }
            
        });
    }
    sjd()
    nex.addEventListener('click',()=>{
        sjd()
        if (start == Number(child.length) ) {
            
            start = start
            
            
        }
        if (start >= Number(child.length) -1 ) {
            nex.style.display="none"
            per.style.display="flex"
            
        }
        checttotel()
        start+= 3
    })
   
  
}



function ajaxdeposite() {
    
fetch(urls +`/${iduser}/`)
.then(res => res.json())
.then(data  =>{
    deposite(data.data)
})
}
ajaxdeposite()


let lis = [1,3,4,5,6,7,8, 9, 10, 11, 12]
let total =lis.length 

// console.log ( Math.round(total) );
console.log (  );

function arradd() {
    let asr = lis.slice(start, end)
    asr.forEach((e, val)=>{
        console.log(e);
    })
}
// arradd()