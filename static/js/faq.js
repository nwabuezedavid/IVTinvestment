const showee =  document.querySelectorAll('.showee')
const hidee =  document.querySelectorAll('.hidee')


showee.forEach((e,we) => {
hidee.forEach((ex,de) => {
    e.addEventListener('click',()=>{
            if (we == de) {
                ex.classList.toggle('hideeshow')

         } else {
            ex.classList.remove('hideeshow')
        
    }
        })
    
});
});


document.addEventListener('scroll',()=>{
      
})