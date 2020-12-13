$(document).ready(function(){
       $('.instagram').on('click',function(){
        $('.searchbar').css({"visibility":"visible","padding":"20px"});
        $('.searchbar form').attr('action','instagram');
    
    });

    $('.youtube').on('click',function(){
        $('.searchbar').css({"visibility":"visible","padding":"20px"});
        $('.searchbar form').attr('action','youtube');
    });

    $('.main a').on('click',function(){
        $(this).html("Downloading...");
    });

    $('.nav-container .instagram').on('click',function(){
        $(this).css({'color':'#6b0000','box-shadow':'0px 0px 12px 1px #cccccc','background':'#fff'});
        $('.nav-container .youtube').css({ 'color':'#ffffff','background': 'linear-gradient(45deg, #a50101,#ff2515)'});
    });
    $('.nav-container .youtube').on('click',function(){
        $(this).css({'color':'#6b0000','box-shadow':'0px 0px 12px 1px #cccccc','background':'#fff'});
        $('.nav-container .instagram').css({'color':"#ffffff",'background': 'linear-gradient(45deg, #a5016e,#c2170b)'});
    });

    // next Page

    $('.nav-container .video').on('click',function(){
        $(this).css({'color':'#6b0000','box-shadow':'0px 0px 12px 1px #cccccc','background':'#fff'});
        $('.nav-container .audio').css({ 'color':'#ffffff','background': 'linear-gradient(45deg, #a50101,#ff2515)'});
        $('.audioContainer').css('display','none');
        $('.videoContainer').css('display','block');
    });
    $('.nav-container .audio').on('click',function(){
        $(this).css({'color':'#6b0000','box-shadow':'0px 0px 12px 1px #cccccc','background':'#fff'});
        $('.nav-container .video').css({ 'color':'#ffffff','background': 'linear-gradient(45deg, #a50101,#ff2515)'}); 
        $('.audioContainer').css('display','block');
        $('.videoContainer').css('display','none');   
    });

    $('table td a').on('click',function(){
        $(this).html("loading...");  
    });
   
    $('.searchbar .form input').on('focus',function(){
        $('.issue , .footer').css('display','none');
    });

    $('.searchbar .form input').on('blur',function(){
        $('.issue , .footer').css('display','block');
    });

});