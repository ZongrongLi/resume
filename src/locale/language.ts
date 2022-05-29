import { getSearchObj } from '@/helpers/location';

/**
 * 获取语言
 */
export function getLanguage(): string {
  const query = getSearchObj();
  const lang = (query.lang as string) || 'en_US';
  typeof document !== 'undefined' && document.body.setAttribute('lang', lang);
  return lang;
}
