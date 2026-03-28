import type { APIRoute } from "astro";

const getRobotsTxt = (sitemapURLs: URL[]) => `
User-agent: *
Allow: /

${sitemapURLs.map(url => `Sitemap: ${url.href}`).join("\n")}
`;

export const GET: APIRoute = ({ site }) => {
  const sitemapURLs = [
    new URL("sitemap.xml", site),
    new URL("sitemap-index.xml", site),
  ];
  return new Response(getRobotsTxt(sitemapURLs));
};
