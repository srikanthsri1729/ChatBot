function getBotResponse() {
    let userText = $("#textInput").val().trim();
    if (!userText) return;

    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);

    $.get("/get", { msg: userText }).done(function(data) {
        let botHtml = '<p class="botText"><span>' + data + '</span></p>';
        $("#chatbox").append(botHtml);
        $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
    });
}

$("#textInput").keypress(function(e) {
    if (e.which == 13) {
        getBotResponse();
    }
});