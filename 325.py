import yfinance as yf
import pandas as pd
import datetime

def check_near_sma(symbols, tolerance=0.05):
  """
  This function checks if a list of stocks are within a certain tolerance of their 325-day SMA.

  Args:
      symbols (list): A list of stock symbols.
      tolerance (float, optional): The percentage tolerance around the SMA. Defaults to 0.05 (5%).

  Returns:
      list: A list of stock symbols that are close to their 325-day SMA.
  """
  near_sma_stocks = []
  for symbol in symbols:
    try:
      # Download data for the past 2 years
      data = yf.download(symbol, period='2y')
      # Calculate 325-day SMA
      data['SMA'] = data['Close'].rolling(window=325).mean()
      # Calculate percentage difference from SMA
      pct_change = (data['Close'] - data['SMA']) / data['SMA']

      # Check if within tolerance and add to results
      if abs(pct_change.iloc[-1]) <= tolerance:
        near_sma_stocks.append(symbol)
    except (yf.DownloadError, KeyError):
      # Handle potential errors during data download or missing data
      pass

  return near_sma_stocks

# Example usage
symbols =  ['SPY', 'QQQ', 'IWM', 'DIA', 'GLD', 'SLV', 'AAPL', 'LHX', 'KEY', 'KRE', 'AMZN', 'GOOG', 'META', 'DXCM', 'TSLA', 'NVDA', 'MSFT', 'JPM', 'BAC', 'WFC', 'C', 'V', 'MA', 'PYPL', 'ADBE', 'CRM', 'NFLX', 'DIS', 'HD', 'MCD', 'NKE', 'SBUX', 'KO', 'PEP', 'PG', 'JNJ', 'UNH', 'PFE', 'MRK', 'ABBV', 'CVS', 'WMT', 'TGT', 'COST', 'LOW', 'TJX', 'M', 'AMT', 'CCI', 'PLD', 'SPG', 'EQIX', 'DLR', 'ARM', 'PSA', 'AVB', 'EQR', 'AIV', 'UDR', 'VTR', 'O', 'WY', 'BXP', 'SLG', 'ARE', 'HST', 'HLT', 'MAR', 'H', 'IHG', 'CCL', 'RCL', 'NCLH', 'LUV', 'UAL', 'DAL', 'AAL', 'ALK', 'EXPE', 'BKNG', 'TRIP', 'SIX', 'FUN', 'PLNT', 'SEAS', 'MGM', 'WYNN', 'LVS', 'ROST', 'BBY', 'TSCO', 'DG', 'DLTR', 'KR', 'TLT', 'XLE', 'XLF', 'XLU', 'XLK', 'XLI', 'XLB', 'XLP', 'XLV', 'XLY', 'XBI', 'XRT', 'XHB', 'XME', 'XSD', 'XSW', 'XITK', 'XNTK', 'XWEB', 'USO', 'AMD', 'INTC', 'MU', 'QCOM', 'TXN', 'AVGO', 'AMAT', 'ADP', 'ADSK', 'ASML', 'BIDU', 'BIIB', 'CDNS', 'CHKP', 'COIN', 'EA', 'EBAY', 'FAST', 'GILD', 'HAS', 'HSIC', 'IDXX', 'ILMN', 'INCY', 'INTU', 'ISRG', 'JBHT', 'KLAC', 'LRCX', 'MCHP', 'MDLZ', 'MNST', 'NTAP', 'NTES', 'XOM', 'CVX', 'GS', 'UNP', 'RTX', 'BA', 'MMM', 'CAT', 'IBM', 'HON', 'VZ', 'LMT', 'GE', 'LLY', 'SMCI', 'SCHW', 'GDX', 'EWZ', 'LIN', 'CSCO', 'DHR', 'UPS', 'BX', 'TMO', 'AMGN', 'MDT', 'BLK', 'PM', 'PNC', 'UBER', 'ABNB', 'NIO', 'TSM', 'SQ', 'ZM', 'DOCU', 'CRWD', 'NET', 'ZS', 'OKTA', 'MDB', 'DDOG', 'SNOW', 'FSLY', 'TWLO', 'ETSY', 'BRK-B', 'GOOGL', 'ACN', 'ABT', 'TMUS', 'COP', 'MS', 'BMY', 'NOW', 'SPGI', 'AXP', 'DE', 'TM', 'ELV', 'NEE', 'SYK', 'MMC', 'VRTX', 'PGR', 'CI', 'REGN', 'CB', 'SLB', 'ADI', 'ETN', 'CME', 'PANW', 'ZTS', 'MO', 'BDX', 'NOC', 'BSX', 'SNPS', 'SO', 'FI', 'WM', 'LULU', 'FDX', 'MSI', 'KHC', 'PLTR', 'TTWO', 'HYG', 'IVV', 'LQD', 'IEF', 'ARKK', 'SOXX', 'QUAL', 'XLRE', 'MSTR', 'ARKG', 'ARKF', 'ARKW', 'PENN', 'SOFI', 'EFA', 'AFRM', 'MARA', 'PDD', 'MELI', 'ANET', 'KWEB', 'T', 'FIVE', 'JWN', 'PSX', 'ITW', 'CCJ', 'ALLE', 'SPOT', 'XYL', 'SNAP', 'ROKU', 'UPST', 'MARA', 'CLSK', 'CURE', 'TD.TO', 'RY.TO', 'BNS.TO', 'BMO.TO', 'CM.TO', 'ENB.TO', 'TRP.TO', 'CNQ.TO', 'SU.TO', 'IMO.TO', 'CP.TO', 'CNR.TO', 'WCP.TO', 'ARX.TO', 'PPL.TO', 'EMA.TO', 'FTS.TO', 'AQN.TO', 'FNV.TO', 'ABX.TO', 'K.TO', 'G.TO', 'FM.TO', 'BCE.TO', 'T.TO', 'RCI-B.TO', 'QSR.TO', 'L.TO', 'MG.TO', 'TOU.TO', 'BIPC.TO', 'BEPC.TO', 'BYD.TO', 'BEP-UN.TO', 'TD.TO', 'RY.TO', 'BNS.TO', 'BMO.TO', 'CM.TO', 'ENB.TO', 'TRP.TO', 'CNQ.TO', 'SU.TO', 'IMO.TO', 'CP.TO', 'CNR.TO', 'WCP.TO', 'ARX.TO', 'PPL.TO', 'EMA.TO', 'FTS.TO', 'AQN.TO', 'FNV.TO', 'ABX.TO', 'K.TO', 'G.TO', 'FM.TO', 'BCE.TO', 'T.TO', 'RCI-B.TO', 'QSR.TO', 'L.TO', 'MG.TO', 'TOU.TO', 'BIPC.TO', 'BEPC.TO', 'BYD.TO', 'BEP-UN.TO', 'AC.TO', 'SHOP.TO', 'QSP-UN.TO', 'TRI.TO', 'BN.TO', 'ATD.TO', 'CSU.TO', 'WCN.TO', 'MFC.TO', 'CVE.TO', 'SLF.TO', 'GWO.TO', 'IFC.TO', 'NA.TO', 'FFH.TO', 'AEM.TO', 'GIB-A.TO', 'NTR.TO', 'DOL.TO', 'WSP.TO', 'TECK-B.TO', 'WPM.TO', 'POW.TO', 'CCO.TO', 'H.TO', 'WN.TO', 'IVN.TO', 'GFL.TO', 'TFII.TO', 'MRU.TO', 'OTEX.TO', 'STN.TO', 'CCL-B.TO', 'SAP.TO', 'TIH.TO', 'DSG.TO', 'FSV.TO', 'CHP-UN.TO', 'X.TO', 'WFG.TO', 'LUN.TO', 'EFN.TO', 'EMP-A.TO', 'IAG.TO', 'CAE.TO', 'IGM.TO', 'ALA.TO', 'CAR-UN.TO', 'ONEX.TO', 'CTC-A.TO', 'GIL.TO', 'MEG.TO', 'KEY.TO', 'CLS.TO', 'PKI.TO', 'CIGI.TO', 'QBR-B.TO', 'AGI.TO', 'DOO.TO', 'PAAS.TO', 'CPG.TO', 'CU.TO', 'PSK.TO', 'NPI.TO', 'CS.TO', 'REI-UN.TO', 'NXE.TO', 'DFY.TO', 'BBD-B.TO', 'FTT.TO', 'ATS.TO', 'ERF.TO', 'GRT-UN.TO', 'BTO.TO', 'BHC.TO', 'CPX.TO', 'SJ.TO', 'ACO-X.TO', 'NVEI.TO', 'LUG.TO', 'TCN.TO', 'BEI-UN.TO', 'OR.TO', 'PBH.TO', 'SRU-UN.TO', 'LNR.TO', 'ATZ.TO', 'MX.TO', 'DIR-UN.TO', 'GEI.TO', 'PRMW.TO', 'TOY.TO', 'FCR-UN.TO', 'ELD.TO', 'SES.TO', 'CRT-UN.TO', 'EQB.TO', 'ATH.TO', 'TPZ.TO', 'BLX.TO', 'FIL.TO', 'CSH-UN.TO', 'HBM.TO', 'TA.TO', 'LSPD.TO', 'MFI.TO', 'CWB.TO', 'GSY.TO', 'CIX.TO', 'WPK.TO', 'RUS.TO', 'VET.TO', 'PEY.TO', 'CRR-UN.TO', 'NVA.TO', 'RCH.TO', 'AP-UN.TO', 'HR-UN.TO', 'EIF.TO', 'AIF.TO', 'KMP-UN.TO', 'ERO.TO', 'STLC.TO', 'DML.TO', 'PXT.TO', 'BBU-UN.TO', 'PET.TO', 'BB.TO', 'FRU.TO', 'TSU.TO', 'IIP-UN.TO', 'CFP.TO', 'TVE.TO', 'IMG.TO', 'EQX.TO', 'FR.TO', 'LIF.TO', 'SVI.TO', 'IPCO.TO', 'ENGH.TO', 'NWC.TO', 'OGC.TO', 'SSL.TO', 'FVI.TO', 'NG.TO', 'LB.TO', 'LAAC.TO', 'KEL.TO', 'ZZZ.TO', 'SIA.TO', 'ES=F', 'NQ=F', 'YM=F', 'RTY=F', 'CL=F', 'GC=F', 'SI=F', 'HG=F', 'ZB=F', 'ZN=F', 'ZT=F', 'ZF=F', 'TN=F', 'ZQ=F', 'GE=F', '6E=F', '6B=F', '6J=F', '6C=F', '6A=F', '6S=F', '6N=F', '6M=F', '6L=F', '6Z=F', 'PL=F', 'QM=F', 'NG=F', 'HO=F', 'RB=F', 'CB=F', 'KC=F', 'CC=F', 'DY=F', 'DC=F', 'GDK=F', 'GNF=F', 'OJ=F', 'YO=F', 'SB=F', 'ZC=F', 'ZO=F', 'ZR=F', 'ZM=F', 'ZL=F', 'ZS=F', 'ZW=F', 'GF=F', 'HE=F', 'LE=F', 'DX=F', 'PA=F']
tolerance = 0.02  # 2% tolerance

near_sma_results = check_near_sma(symbols, tolerance)

# Get today's date
today = datetime.date.today()

# Create a file name with today's date
file_name = f"{today}.txt"

# Write the data to the file
with open(file_name, "w") as file:
    if near_sma_results:
        file.write("Stocks close to their 325-day SMA:\n")
        for stock in near_sma_results:
            file.write(stock + "\n")
    else:
        file.write("No stocks found close to their 325-day SMA within the tolerance level.")
