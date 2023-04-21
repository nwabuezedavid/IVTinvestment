const notificationicon = document.querySelector('.notificationicon')
const parent__ulA = document.querySelectorAll('.parent__ulA')
const child__ulA = document.querySelectorAll('.child__ulA')

notificationicon.addEventListener("click", ()=>{
    alert("check your message box ")
})
parent__ulA.forEach((e, vl) => {
         e.addEventListener("click", ()=>{


 child__ulA.forEach((ed, val) => {
    if (vl == val) {
                     ed.classList.toggle("child__ulADisable")
                     
        }else{
                    ed.classList.add("child__ulADisable")

                }
})
})
})



child__ulA.forEach((ed, val) => {

             ed.classList.add("child__ulADisable")
           
 })