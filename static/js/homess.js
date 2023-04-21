// const input__plan__planSele = document.querySelector(".planSele")
const input__plan__outcome = document.querySelector(".outcome")
const input__plan__imput__amount = document.querySelector(".imput__amount")
// const body = document.querySelector("body")


 

console.log(location.pathname);
if (location.pathname == '/html/home.html') {
    
input__plan__imput__amount.addEventListener('keyup', ()=>{
    if (input__plan__planSele.value == 'basic' && input__plan__imput__amount.value >= 100 &&  input__plan__imput__amount.value <= 999) {
            
            var percent = 10;
            var daily = Number(input__plan__imput__amount.value )/100*percent;
            daily =  daily.toFixed(2);
            input__plan__outcome.textContent =  daily
            
      

    }
   
  
    else if (input__plan__planSele.value == 'diamond') {
        if (input__plan__imput__amount.value >= 100000 && input__plan__imput__amount.value <= 1000000999000) {
            
            var percent = 100;
            var daily = Number(input__plan__imput__amount.value )/100*percent;
            daily =  daily.toFixed(2);
            input__plan__outcome.textContent =  daily
            
        }else{
            input__plan__outcome.textContent =  "N/A"

        }
        
    }
    else if (input__plan__planSele.value == 'gold') {
        if (input__plan__imput__amount.value >= 50000 && input__plan__imput__amount.value <= 99000) {
            
            var percent = 50;
            var daily = Number(input__plan__imput__amount.value )/100*percent;
            daily =  daily.toFixed(2);
            input__plan__outcome.textContent =  daily
            
        }else{
            input__plan__outcome.textContent =  "N/A"

        }
    }
    else if (input__plan__planSele.value == 'sliver'  ) {
        if (input__plan__imput__amount.value >= 1000 && input__plan__imput__amount.value <= 49000) {
            
            var percent = 30;
            var daily = Number(input__plan__imput__amount.value )/100*percent;
            daily =  daily.toFixed(2);
            input__plan__outcome.textContent =  daily
            console.log(daily);
            
        }else{
            input__plan__outcome.textContent =  "N/A"

        }
    }else{
        input__plan__outcome.textContent =  "N/A"

    }
})


}






const observer = new IntersectionObserver((entries) =>{
    entries.forEach((entry) =>{
        if (entry.isIntersecting ) {
            entry.target.classList.add('showas')
        }else{
            entry.target.classList.remove('showas')

        }
    })
})

let allAnim = document.querySelectorAll('.ano')
allAnim.forEach((el)=>{
    observer.observe(el)
})



const cont_holiding = document.querySelector('.first-link-con')
const navBtn = document.querySelector('.click-nav')
const ponzx = document.querySelector('.sec-4-wrapper2')
const media_con = document.querySelector('.sec-5-con')
const media_con2 = document.querySelector('.over-lay')
let size_s = media_con.clientHeight
let size_s2 = media_con2.clientHeight
const media_con_media = document.querySelector('.ssd')
const artic= document.querySelectorAll('.hiiden')
const readermore= document.querySelectorAll('.readermore')

// const p0pular_con = document.querySelectorAll('.post-im-wrapper')
const p0pular_img = document.querySelectorAll('.hiddx')
const p0pular_letter = document.querySelectorAll('.hidd')

let ini = 0

function testimponal() {
    ini++
    p0pular_img.forEach((e,val)=>{
if (val == ini) {
    e.classList.add('show-acx')
    e.style.transition=  "all 3s cubic-bezier(0.075, 0.82, 0.165, 1) "
    
}else if (ini == p0pular_img.length ){
    ini = 0
    e.classList.add('show-acx')
}

else{
    setTimeout(() => {
        e.classList.remove('show-acx')
        e.style.transition=  "all 3s cubic-bezier(0.075, 0.82, 0.165, 1) "
        
    }, 200);
}
    })


    p0pular_letter.forEach((es,vasl)=>{
if (vasl == ini) {
    es.classList.add('show-ac')
    es.style.transition='all 2s cubic-bezier(0.075, 0.82, 0.165, 1) linear ' 


    console.log('hee',es);
}else if (ini == p0pular_img.length ){
    // ini = 0
    es.classList.add('show-ac')
}
else{
    
    setTimeout(() => {
        es.classList.remove('show-ac')
        
    }, 230);
}
    })

   

}


setInterval(() => {
    
    testimponal()
}, 14000);


if (location.pathname == '/user__dashboard/deposite.html'){
readermore.forEach((e,val) => {
    artic.forEach((ex,valx) => {
    
        
        e.addEventListener('click',()=>{
            if (val == valx) {
            ex.classList.add('shows')
            
        } 
    else {
        ex.classList.remove('show')

    }
        })
    
    })
});





let sd = Number(size_s) / 2


function positionMedia() {
    media_con_media.style.height = `${57 + 'pc'}`
    // media_con_media.style.height = `${Number(size_s) + sd - 920 +'px'}`
    // media_con_media.style.height = `${Number(size_s)} + 'px'`
}

positionMedia()




// sponsor

const sponChi= document.querySelectorAll('.child-sec-6')
const sponCh_icon_count= document.querySelectorAll('.hide-i')
let sponCount = 0

function click_spon() {
    
    sponChi.forEach((e, vd) => {
    sponCh_icon_count.forEach((es,vals) => {
            e.classList.add('child-6-show')
            if (vd == vals){
            }else{
          
                e.classList.remove('child-6-show')
            }
        })
    });
}




click_slide_spON()
function sponslide() {
    sponCount++

    sponCh_icon_count[0].classList.add('show-act-i')
    sponCh_icon_count.forEach((ea,vak) => {
       
        if (vak == sponCount) {
               ea.classList.add('show-act-i')
            }else{
            ea.classList.remove('show-act-i')

        }
   
    sponChi.forEach((e,val) => {
        if (val == sponCount) {
            e.classList.add('child-6-show')
        }else if (sponCount == sponChi.length ) {
            e.classList.add('child-6-show')
            sponCount = 0
            
        }
        else{
            setTimeout(() => {
                
                e.classList.remove('child-6-show')
            }, 300);

        }
        
    });
 });
}
// sponslide()


let cleard = setInterval(() => {
    sponslide()
}, 12000);

function click_slide_spON() {
    clearInterval()

    sponChi.forEach((e, vd) => {
        sponCh_icon_count.forEach((es,vals) => {
        es.addEventListener('click',()=>{

            if (vd == sponCount){
                e.classList.add('child-6-show')
                // sponCount = Number(vd)
                    es.classList.add('show-act-i')
                  

            }else{
                e.classList.remove('child-6-show')
                console.log(es.className);
                es.classList.remove('show-act-i')
            }

        });
        });
    });
}

}