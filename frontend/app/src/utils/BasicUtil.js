class BasicUtil {
  /**
   * Method used to compose new array for select optgroup
   */
  static buildOptGroup(items, group_key) {
    let optGrouped = {};
    for(const item of items) {
      const tempGroupKey = item[group_key];
      if (Object.keys(optGrouped).includes(tempGroupKey) == true) {
        optGrouped[tempGroupKey].push(item);
      } else {
        optGrouped[tempGroupKey] = [item];
      }
    }

    return optGrouped;
  };
}

export default BasicUtil;
