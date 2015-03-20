public class ExcelSheet {
	
	public String convertToTitle(int n) {
        StringBuffer buffer = new StringBuffer();
		excelSheet(n, buffer);
		return buffer.toString();
    }
    
    public void excelSheet(int n, StringBuffer buffer){
		if( n < 1 ){
			return;
		}
		int moduleNum = n%26;
		
		if(moduleNum == 0){
		    excelSheet(n/26-1, buffer);
		    buffer.append('Z');
		    
		}else{
		    excelSheet(n/26, buffer);
		    buffer.append((char)(moduleNum + 64));
		}
	
		return;
	}
    
  
}