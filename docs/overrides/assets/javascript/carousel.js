import Flicking from 'https://cdn.jsdelivr.net/npm/@egjs/flicking@4.12.0/+esm'

document$.subscribe(() => {
    const carousel = document.getElementById('carousel')
    
    if (carousel) {
        const flicking = new Flicking(carousel, {
            align: "center",
            circular: true,
            bound: true,
            renderOnlyVisible: true
        });

        flicking.on('select', ({ panel }) => {
            const anchor = panel.element.querySelector('a')
            if (anchor) anchor.click();
        })
    }
})

