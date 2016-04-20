import { reduce, omit, keys } from 'lodash';
import qs from 'qs';
import { parse } from 'url';

const rxClean = /(\(:[^\)]+\)|:[^\/]+)/g;

export default function urlTransform(url, params={}) {
  if (!url) { return ''; }
  const usedKeys = {};
  const urlWithParams = reduce(params,
    (url, value, key)=> url.replace(
      new RegExp(`(\\(:${key}\\)|:${key})`, 'g'),
        ()=> (usedKeys[key] = value)), url);
  if (!urlWithParams) { return urlWithParams; }
  const { protocol, host, path } = parse(urlWithParams);
  const cleanURL = (host) ?
    `${protocol}//${host}${path.replace(rxClean, '')}` :
    path.replace(rxClean, '');
  const usedKeysArray = keys(usedKeys);
  if (usedKeysArray.length !== keys(params).length) {
    const urlObject = cleanURL.split('?');
    const mergeParams = {
      ...(urlObject[1] && qs.parse(urlObject[1])),
      ...omit(params, usedKeysArray)
    };
    return `${urlObject[0]}?${qs.stringify(mergeParams)}`;
  }
  return cleanURL;
}
