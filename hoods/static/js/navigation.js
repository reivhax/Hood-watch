navigate=(event)=>{
    let url = event.currentTarget.attributes['route'].value;
    let old = location.pathname;
    $('#sidebar').toggleClass('side',250);
    $("[route='"+old+"']").removeClass("active");
    $("[route='"+url+"']").addClass("active");
    history.pushState('','',url);
    $.get(url,'',(data)=>{
        $("body" ).empty();
        $("body" ).append(data);
        rebind()
    })
};
rebind=()=>{
    $('.navigation').unbind('click',navigate);
    $('.navigation').click(navigate);
    $("#id_description").attr('rows','1');
    $("form").attr('autocomplete','off');
};
$(document).ready(rebind);