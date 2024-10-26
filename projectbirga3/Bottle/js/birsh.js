document.getElementById('themeToggle').addEventListener('click', function() {
    const currentTheme = document.body.className;
    if (currentTheme === 'light-theme') {
        document.body.className = 'dark-theme';
    } else {
        document.body.className = 'light-theme';
    }
});


// Изменение цены с каждым тиком

price = document.getElementsByClassName('emerald-price')[0] // <div class="emerald-price">


async function emeraldChanger() {
  for (let i = 0; i < 10; i++) {
    await new Promise(r => setTimeout(r, 2000));
    console.log('1');
    price.textContent = i.toString();
  }
}

emeraldChanger();