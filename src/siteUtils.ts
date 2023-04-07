const defaultSiteKey = 'tvb-ext-xircuits:defaultSite';

export function writeDefaultSite(site: string): void {
  localStorage.setItem(defaultSiteKey, site);
}

export function readDefaultSite(): string {
  return localStorage.getItem(defaultSiteKey);
}
