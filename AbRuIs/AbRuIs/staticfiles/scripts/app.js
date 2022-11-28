$(document).ready(function(){
    
    var loader = document.getElementById('chart-preloader');
    setTimeout(function(){
        loader.style.display = "none";
    },1000)
    $('canvas').hide()
    $('#myChart5').show()
    $('#c-btn1').click(function(){
        loader.style.display = 'flex'
        setTimeout(function(){
            loader.style.display = "none";
        },1000)
        $('canvas').hide()
        $('#myChart').show();
    })
    $('#c-btn2').click(function(){
        loader.style.display = 'flex'
        setTimeout(function(){
            loader.style.display = "none";
        },1000)
        $('canvas').hide()
        $('#myChart2').show();
        
    })
    $('#c-btn3').click(function(){
        loader.style.display = 'flex'
        setTimeout(function(){
            loader.style.display = "none";
        },1000)
        $('canvas').hide()
        $('#myChart3').show();
    })
    $('#c-btn4').click(function(){
        loader.style.display = 'flex'
        setTimeout(function(){
            loader.style.display = "none";
        },1000)
        $('canvas').hide()
        $('#myChart4').show();
    })
    $('#c-btn5').click(function(){
        loader.style.display = 'flex'
        setTimeout(function(){
            loader.style.display = "none";
        },1000)
        $('canvas').hide()
        $('#myChart5').show();
    })
})