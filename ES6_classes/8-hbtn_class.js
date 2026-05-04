export default class HolbertonClass {

  constructor(size, location) {
    this.size = size
    this.location = location
  }

  [Symbol.toPrimitive](value) {
    if (value === 'number') {
      return this._size;
    }

    if (value === 'string') {
      return this._location;
    }
  }
}
