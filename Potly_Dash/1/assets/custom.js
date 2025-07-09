(function waitForDash()
{
    const button1      = document.getElementById('button1');
    const floating_div = document.getElementById('floating_div');
    const all_exists   = button1 && floating_div;

    if(all_exists)
    {
        button1.addEventListener('click', () => {
            floating_div.style.visibility = 'visible';
            floating_div.classList.toggle('clicked');
        });
    }
    else // try again in 100ms;
        setTimeout(waitForDash, 100);
})();