import type { Props } from '@astrojs/starlight/props';

export default function (props: Props): Props {
    return {
        ...props,
        hasSidebar: props.entry.data.template === "doc",
        toc: props.entry.data.template === "doc" ? props.toc : undefined,
    }
}