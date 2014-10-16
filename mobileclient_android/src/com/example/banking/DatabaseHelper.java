package com.example.banking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

final class DatabaseHelper extends SQLiteOpenHelper {

	private static final String DATABASENAME = "bankingdb";
	private Context context;
	
	DatabaseHelper(Context context) {
		super(context, DATABASENAME, null, 1);
		this.context = context;
	}

	@Override
	public void onCreate(SQLiteDatabase db) {
		// Create database structure
		try {
			insertFromFile(db, context, R.raw.db);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public void onUpgrade(SQLiteDatabase db, int arg1, int arg2) {
		// TODO Auto-generated method stub
	}

	/**
	 * This reads a file from the given Resource-Id and calls every line of it
	 * as a SQL-Statement
	 * 
	 * @param context
	 * 
	 * @param resourceId
	 * 
	 * @return Number of SQL-Statements run
	 * @throws IOException
	 */
	public static int insertFromFile(SQLiteDatabase db, Context context, int resourceId)
			throws IOException {
		// Reseting Counter
		int result = 0;

		// Open the resource
		InputStream insertsStream = context.getResources().openRawResource(
				resourceId);
		BufferedReader insertReader = new BufferedReader(new InputStreamReader(
				insertsStream));

		// Iterate through lines (assuming each insert has its own line and
		// there's no other stuff)
		while (insertReader.ready()) {
			String insertStmt = insertReader.readLine();
			db.execSQL(insertStmt);
			result++;
		}
		insertReader.close();

		// Returning number of inserted rows
		return result;
	}
}
