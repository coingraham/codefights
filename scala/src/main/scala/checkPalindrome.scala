object checkPalindrome extends App {

  def checkPalindrome(inputString: String): Boolean = {
    inputString == inputString.reverse
  }

  println(checkPalindrome("testtset"))

}
