const create__paymencard = document.querySelector('.create__paymencard')
const add__cardbtn = document.querySelector('.add__cardbtn')

add__cardbtn.addEventListener('click',()=>{
    create__paymencard.classList.toggle("visableCrete")
    if (create__paymencard.classList.contains('visableCrete')) {
        
        alert('You can create a new card for payment.')
    }
})