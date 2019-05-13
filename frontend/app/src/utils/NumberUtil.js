class NumberUtil {
  /**
   * Method used to format number as currency
   */
  static currencyFormatter(value) {
    const formatter = new Intl.NumberFormat('en-Us', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2,
    });

    return formatter.format(value);
  }
}

export default NumberUtil;
