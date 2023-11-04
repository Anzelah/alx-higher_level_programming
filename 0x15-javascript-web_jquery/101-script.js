document.addEventListener("DOMContentLoaded", () => {
  var item = '<li>Item</li>';
  $('#add_item').click(function() {
    $('UL.my_list').append(item);
  });
  $('#remove_item').click(function() {
    $('UL.my_list li:last').remove();
  });
  $('#clear_list').click(function() {
    $('UL.my_list').empty();
  });
});
