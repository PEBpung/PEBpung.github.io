interface Window {
  __backButtonBound?: boolean;
  __backToTopScrollHandler?: EventListener;
  __headerNavBound?: boolean;
  __indexBackUrlBound?: boolean;
  __mainBackUrlBound?: boolean;
  __scrollHandler?: EventListener;
  theme?: {
    themeValue: string;
    setPreference: () => void;
    reflectPreference: () => void;
    getTheme: () => string;
    setTheme: (val: string) => void;
  };
}
