function onMonsterClick(id) {
    console.log(id, "monster was clicked ");
    const rid = id.substring(8);
    const monster = document.getElementById(id);
    
    if (monster.classList.contains("active")) {
        monster.classList.remove("active");

        const display = document.getElementById("info_" + rid);
        if (!display.classList.contains("hidden")) display.classList.add("hidden");
    } else {
        monster.classList.add("active");

        const display = document.getElementById("info_" + rid);
        if (display.classList.contains("hidden")) display.classList.remove("hidden");
    }
}

function exitInfo(id) {
    console.log("closing display");
    const rid = id.substring(7);
    const display = document.getElementById("info_" + rid);
    if (!display.classList.contains("hidden")) display.classList.add("hidden");

    const monster = document.getElementById("monster_" + rid);
    if (monster.classList.contains("active")) monster.classList.remove("active");
}