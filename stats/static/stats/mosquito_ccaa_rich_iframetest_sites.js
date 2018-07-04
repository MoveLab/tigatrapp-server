var getCheckedCategories = function(){
    var checked_list = [];
    var categories = ['storm_drain_water','storm_drain_dry','breeding_site_other'];
    for(var i = 0; i < categories.length; i++){
        var checked = $('#' + categories[i]).prop('checked');
        if(checked){
            checked_list.push(categories[i]);
        }
    }
    return checked_list;
}

var showPanel = function(category){
    var checked_categories = getCheckedCategories();
    var filter_array = [];
    for( var i = 0; i < checked_categories.length; i++){
        filter_array.push('#' + checked_categories[i]);
    }
    filter_string = filter_array.join(',');
    if(filter_string != ''){
        $grid.isotope({ filter: filter_string });
    }else{
        $grid.isotope({ filter: '#kk' });
    }
}

var hideLoader = function(div_id){
    $('#' + div_id + " .progress").hide();
}

$( document ).ready(function() {
//$(function () {

    $grid = $('.grid').isotope({
        layoutMode: 'fitRows',
        itemSelector: '.grid-item'
    });
    $grid.isotope({ filter: '#kk' });

    $("#categories").append('<li><input id="storm_drain_water" onclick="javascript:showPanel(\'storm_drain_water\')" type="checkbox">Breeding sites with water</li>');
    $("#categories").append('<li><input id="storm_drain_dry" onclick="javascript:showPanel(\'storm_drain_dry\')" type="checkbox">Breeding sites without water</li>');
    $("#categories").append('<li><input id="breeding_site_other" onclick="javascript:showPanel(\'breeding_site_other\')" type="checkbox">Other breeding sites</li>');


    $('#storm_drain_water_iframe').attr('src','/stats/mosquito_ccaa_rich/storm_drain_water');
    $('#storm_drain_dry_iframe').attr('src','/stats/mosquito_ccaa_rich/storm_drain_dry');
    $('#breeding_site_other_iframe').attr('src','/stats/mosquito_ccaa_rich/breeding_site_other');

    $("#storm_drain_water_iframe").on('load',function(){
        hideLoader('storm_drain_water');
    });

    $("#storm_drain_dry_iframe").on('load',function(){
        hideLoader('storm_drain_dry');
    });

    $("#breeding_site_other_iframe").on('load',function(){
        hideLoader('breeding_site_other');
    });

});