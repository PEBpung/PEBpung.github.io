export const SITE = {
  website: "https://pebpung.github.io/",
  author: "pebpung",
  profile: "https://github.com/PEBpung",
  desc: "ML감자 - AI Engineer Blog",
  title: "ML감자",
  ogImage: "astropaper-og.jpg",
  lightAndDarkMode: true,
  postPerIndex: 6,
  postPerPage: 6,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: true,
  showBackButton: true,
  editPost: {
    enabled: false,
    text: "Edit page",
    url: "https://github.com/PEBpung/PEBpung.github.io/edit/astro/src/data/blog/",
  },
  dynamicOgImage: true,
  dir: "ltr",
  lang: "ko",
  timezone: "Asia/Seoul",
} as const;

export const PROFILE = {
  username: "pebpung",
  description: "AI Engineer at BHSN",
  image: "/assets/img/profile/ocean.jpeg",
} as const;
