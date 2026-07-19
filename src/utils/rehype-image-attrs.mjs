import { visit } from "unist-util-visit";

/**
 * rehype plugin: add native lazy-loading and async decoding to every
 * markdown `<img>` so off-screen images (most of a long post) don't block
 * the initial page load. These posts reference raw `/assets/img/...` paths
 * that bypass Astro's image pipeline, so we set the hints here instead.
 */
export default function rehypeImageAttrs() {
  return tree => {
    visit(tree, "element", node => {
      if (node.tagName !== "img") return;
      node.properties = node.properties || {};
      // Respect any attributes an author set explicitly in the source.
      if (node.properties.loading == null) node.properties.loading = "lazy";
      if (node.properties.decoding == null) node.properties.decoding = "async";
    });
  };
}
