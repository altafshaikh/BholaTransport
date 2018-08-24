$( document ).ready(function( $ ) {
  jQuery( '#example1' ).sliderPro({
    width: 960,
    height: 500,
    arrows: true,
    buttons: false,
    waitForLayers: true,
    thumbnailWidth: 200,
    thumbnailHeight: 100,
    thumbnailPointer: true,
    autoplay: false,
    autoScaleLayers: false,
    breakpoints: {
      500: {
        thumbnailWidth: 120,
        thumbnailHeight: 50
      }
    }
  });
});