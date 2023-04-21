const count_load = document.querySelector('.count_loads')
const hides_btn = document.querySelector('.hides_btn')


let  normal_coun = 0


function loader() {
    count_load.innerHTML = normal_coun 
     normal_coun++

}

setInterval(() => {
    if ( normal_coun == 101 ) {
         normal_coun = 100
         hides_btn.classList.add('show')
        } else {
            loader()
        
    }
}, 20);