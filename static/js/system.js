$("#double-dice-roller").submit(function(event) {
    event.preventDefault();
    var $critical = $("#double-dice-roller [data-id=critical-label]");
    $critical.hide();

    var result1 = Math.floor(Math.random() * 10) + 1;
    var result2 = Math.floor(Math.random() * 10) + 1;
    var biggest;
    if (result1 >= result2)
        biggest = result1;
    else
        biggest = result2;

    $("#double-dice-roller [data-id=result-one]").text(result1);
    $("#double-dice-roller [data-id=result-two]").text(result2);
    $("#double-dice-roller [data-id=results-biggest]").text(biggest);

    if ((result1 + result2) >= 18) {
        $critical.show();
    }

    $("#double-dice-result").show();
});

$("#dice-roller").submit(function(event) {
    event.preventDefault();
    var result = Math.floor(Math.random() * 10) + 1;
    $("#dice-roller [data-id=result]").text(result);
    $("#dice-result").show();
});

function setSubmitHandlerBy(attribute) {
    $("#" + attribute).submit(function(event) {
        event.preventDefault();

        var $modifier = $("#" + attribute + " [name=modifier]");
        var modifier;
        if ($modifier.val())
            modifier = parseInt($modifier.val(), 10);
        else
            modifier = 0;

        var $resultLabel = $("#" + attribute + " [data-id=result-label]");
        var $result = $("#" + attribute + " [data-id=result-value]");
        var $bonusLabel = $("#" + attribute + " [data-id=bonus-label]");
        var $bonus = $("#" + attribute + " [data-id=bonus-value]");

        var ofensive = parseInt($("#" + attribute + " [name=ofensive]").val(), 10) + modifier;
        var defensive = parseInt($("#" + attribute + " [name=defensive]").val(), 10);
        var result = ofensive - defensive;

        var klass = '';
        var label = '';
        if (result > 0) {
            klass = 'success';
            label = 'Passou!';
        } else if (result < 0) {
            klass = 'important';
            label = 'Não passou.';
        }
        else {
            klass = 'inverse';
            label = 'Empate.';
        }

        $resultLabel.text(label).attr('class', 'label label-' + klass);
        $result.text(result).attr('class', 'badge badge-' + klass);

        var bonus = calculateBonus(result);
        $bonusLabel.attr('class', 'label label-' + klass);
        $bonus.text(bonus).attr('class', 'badge badge-' + klass);
        $("#" + attribute + " [data-id=result-block]").show();

        // Carry over bonus of accuracy to damage
        if (attribute == 'accuracy') {
            $("#damage [name=modifier]").val(bonus);
        }
    });
}

setSubmitHandlerBy('accuracy');
setSubmitHandlerBy('damage');

function calculateBonus(value) {
    var bonus;
    if (value <= 0) return 0;
    if (value % 2 !== 0) {
        value = value + 1;
    }
    bonus = (value / 2) - 1;
    return bonus;
}
