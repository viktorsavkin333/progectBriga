<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>birsh</title>
    <link rel="stylesheet" href="css/birsh.css">
</head>
<body>
    <button id="themeToggle">Переключить тему</button>
    <div class="logo">
        <button onclick="window.location.href = 'profile.html'">
            <img src="src/icon_profile.png" alt="">
        </button>
    </div>
    <div class="buttons_resourse">
        <button class="btn1">
            Iron
        </button>
        <button class="btn2">Gold</button>
        <button class="btn3">
            <div class="btn_text">
                Emerald
            </div> 
            <img class="btn_img" src="src/emerald.png" alt="">
            <div>
              Цена 1шт.: 
              <div class="emerald-price">
                {{emerald_price}}
              </div>
            </div>
        </button>
        <button class="btn4">Quartz</button>
        <button class="btn5">Nezerite</button>
    </div>
    <script src="js/birsh.js"></script>
</body>
</html>
